package TP2.ex3.ex3_2;

import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class CreateXMLFileJava {
   public static final String xmlFilePath = "xmlfile.xml";

   public static void main(String argv[]) {

      try {
         File inputFile = new File(xmlFilePath);// Create DocumentBuilderFactory object.
         DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
         DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
         Document document = dBuilder.parse(inputFile);
         for (int i = 0; i < argv.length; i++) {
            
            Node employee = document.getElementsByTagName("employee").item(i);
            NodeList list = employee.getChildNodes();
            for (int temp = 0; temp < 4; temp++) {
               Node node = list.item(temp);
               if (node.getNodeName().equals("salaire"))
                  node.setTextContent("3000");
            }
         }

         // Save changes into XML file.
         TransformerFactory transformerFactory = TransformerFactory.newInstance();
         Transformer transformer = transformerFactory.newTransformer();
         DOMSource source = new DOMSource(document);
         StreamResult result = new StreamResult(new File(xmlFilePath));
         transformer.transform(source, result);

         // For console Output.
         StreamResult consoleResult = new StreamResult(System.out);
         transformer.transform(source, consoleResult);
      } catch (Exception e) {
         e.printStackTrace();
      }
   }
}
