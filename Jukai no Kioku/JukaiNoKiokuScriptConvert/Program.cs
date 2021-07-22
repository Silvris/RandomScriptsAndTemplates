using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Xml;

namespace JukaiNoKiokuScriptConvert
{
    class Program
    {
        public static string ReadUniNullTerminatedString(BinaryReader br)
        {
            List<byte> stringC = new List<byte>();
            byte newByte = br.ReadByte();
            byte newByte2 = br.ReadByte();
            while (newByte != 0 || newByte2 != 0)
            {
                stringC.Add(newByte);
                stringC.Add(newByte2);
                newByte = br.ReadByte();
                newByte2 = br.ReadByte();
            }
            return Encoding.Unicode.GetString(stringC.ToArray());//has to be Unicode, as all text is in Japanese Unicode (*not* Shift-JIS)
        }
        public static void WriteUniNullTerminatedString(BinaryWriter bw, string str)
        {
            bw.Write(Encoding.Unicode.GetBytes(str.ToCharArray()));
            bw.Write((Int16)0);
        }

        public static void BinToXml(string filename)
        {
            List<ScriptEvent> scriptEvents = new List<ScriptEvent>();
            BinaryReader br = new BinaryReader(new FileStream(filename, FileMode.Open));
            for (int i = 0; i < 3; i++)
            {
                br.ReadInt32();//three uints of buffer at the start of every file
            }
            int eventCount = br.ReadInt32();
            for (int i = 0; i < eventCount; i++)
            {
                ScriptEvent se = new ScriptEvent();//this is why it only has a default constructor and xml constructor
                se.unknHead = br.ReadInt16();
                se.eventType = br.ReadInt16();
                se.eventActor = br.ReadInt16();
                se.eventAction = br.ReadInt16();
                for (int j = 0; j < 12; j++)
                {
                    se.unkns1[j] = br.ReadInt16();
                }
                se.eventValue = br.ReadInt16();
                for (int j = 0; j < 23; j++)
                {
                    se.unkns2[j] = br.ReadInt16();
                }
                scriptEvents.Add(se);
            }
            //go through all of the script events to get to the string data
            long stringOffset = br.BaseStream.Position;
            //now read strings for any type1
            for (int i = 0; i < scriptEvents.Count; i++)
            {
                if (scriptEvents[i].eventType == 0x1)
                {
                    br.BaseStream.Seek(stringOffset + scriptEvents[i].eventValue, SeekOrigin.Begin);
                    scriptEvents[i].eventText = ReadUniNullTerminatedString(br);
                    scriptEvents[i].eventText = scriptEvents[i].eventText.Replace("\n", "\\n");
                    scriptEvents[i].eventText = scriptEvents[i].eventText.Replace("\r", "\\r");
                }
            }
            //now export to xml
            XmlWriterSettings settings = new XmlWriterSettings();
            settings.Indent = true;
            settings.Encoding = Encoding.Unicode;
            settings.OmitXmlDeclaration = true;
            XmlWriter xml = XmlWriter.Create(filename.Replace(".bin", ".xml"), settings);
            xml.WriteStartElement("JukaiNoKiokuScript");
            for (int i = 0; i < scriptEvents.Count; i++)
            {
                scriptEvents[i].ExportXml(xml);
            }
            xml.WriteEndElement();
            xml.Close();
            return;
        }

        static void Main(string[] args)
        {
            if(args.Length > 0)
            {
                for(int i = 0; i < args.Length; i++)
                {
                    if (args[i].Contains(".bin"))
                    {
                        BinToXml(args[i]);
                    }
                    else if (args[i].Contains(".xml"))
                    {

                    }
                }
                
            }
            else
            {
                Console.WriteLine("Run in command-line with the path of the file following, or just drop it onto the exe.");
            }
        }
    }
}
