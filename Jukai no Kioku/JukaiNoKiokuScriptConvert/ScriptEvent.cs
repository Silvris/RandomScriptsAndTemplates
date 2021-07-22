using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Xml;

namespace JukaiNoKiokuScriptConvert
{
    class ScriptEvent
    {
        public short unknHead;
        public short eventType;
        public short eventActor;
        public short eventAction;
        public short[] unkns1;
        public short eventValue;
        public string eventText;
        public short[] unkns2;

        public ScriptEvent(XmlReader xml)
        {
            if(xml.Name == "ScriptEvent")
            {
                while (xml.Read())
                {

                    switch (xml.Name)
                    {
                        case "unknHead":
                            unknHead = (short)xml.ReadElementContentAsInt();
                            break;
                        case "eventType":
                            eventType = (short)xml.ReadElementContentAsInt();
                            break;
                        case "eventActor":
                            eventActor = (short)xml.ReadElementContentAsInt();
                            break;
                        case "eventAction":
                            eventAction = (short)xml.ReadElementContentAsInt();
                            break;
                        case "unkns1":
                            unkns1 = (short[])xml.ReadContentAs(typeof(short[]), null);
                            break;
                        case "eventValue":
                            eventValue = (short)xml.ReadElementContentAsInt();
                            break;
                        case "eventText":
                            eventText = xml.ReadElementContentAsString();
                            break;
                        case "unkns2":
                            unkns2 = (short[])xml.ReadContentAs(typeof(short[]), null);
                            break;
                    }
                }
            }
            
        }

        public ScriptEvent()
        {
            unknHead = 99;
            eventType = 0;
            eventActor = -1;
            eventAction = -1;
            unkns1 = new short[12] { -1, -1, 32767, 0, 0, 0, 0, 0, 0, 0, 0, 0};
            eventValue = 0;
            unkns2 = new short[23] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
            eventText = "";//most don't use this
        }
        public void Export(BinaryWriter bw)
        {
            bw.Write(unknHead);
            bw.Write(eventType);
            bw.Write(eventActor);
            bw.Write(eventAction);
            for(int i = 0; i < 12; i++)
            {
                bw.Write(unkns1[i]);
            }
            bw.Write(eventValue);
            for (int i = 0; i < 23; i++)
            {
                bw.Write(unkns2[i]);
            }
            //text is output later
        }
        public void ExportXml(XmlWriter xml)
        {
            xml.WriteStartElement("ScriptEvent");
            xml.WriteElementString("unknHead", unknHead.ToString());
            xml.WriteElementString("eventType", eventType.ToString());
            xml.WriteElementString("eventActor", eventActor.ToString());
            xml.WriteElementString("eventAction", eventAction.ToString());
            xml.WriteStartElement("unkns1");
            xml.WriteValue(unkns1);
            xml.WriteEndElement();
            if(eventText != "")
            {
                xml.WriteElementString("eventText", eventText);
            }
            else
            {
                xml.WriteElementString("eventValue", eventValue.ToString());
            }
            xml.WriteStartElement("unkns2");
            xml.WriteValue(unkns2);
            xml.WriteEndElement();
            xml.WriteEndElement();
        }
    }
}
