package TP2.ex3.ex3_1;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class CreateXMLFileJava { 
    public static final String xmlFilePath = "xmlfile.xml";
    public static void main(String argv[]) {
   
    try {

    DocumentBuilderFactory documentFactory =
    DocumentBuilderFactory.newInstance();
   
    DocumentBuilder documentBuilder = documentFactory.newDocumentBuilder();
   
    Document document = documentBuilder.newDocument();
    // root element
    Element root = document.createElement("company");
    document.appendChild(root);
    List<Employe> listemp = new ArrayList<>();
    listemp.add(new Employe("Amin", "Trigui", 30, 2500));
    listemp.add(new Employe("Salah", "Chaari", 22, 1500));
    listemp.add(new Employe("Amir", "Ben Fraj", 24, 2000));
    listemp.add(new Employe("Ahmed", "Frikha", 24, 2250));
    for (int i = 0; i < 4; i++) {
        
    
    // employee element
    Element employee = document.createElement("employee");
   
    root.appendChild(employee);
   
    // set an attribute to staff element
    Attr attr = document.createAttribute("id");
    attr.setValue(listemp.get(i).getId());
    employee.setAttributeNode(attr);
   
    //you can also use staff.setAttribute("id", "1") for this
   
    // firstname element
    Element firstName = document.createElement("firstname");
    firstName.appendChild(document.createTextNode(listemp.get(i).getFirstname()));
    employee.appendChild(firstName);
   
    // lastname element
    Element lastname = document.createElement("lastname"); 
    lastname.appendChild(document.createTextNode(listemp.get(i).getLastname()));
 employee.appendChild(lastname);

 // age element
 Element age = document.createElement("age");
 age.appendChild(document.createTextNode(listemp.get(i).getAge()));
 employee.appendChild(age);

 // salaire elements
 Element salaire = document.createElement("salaire");
 salaire.appendChild(document.createTextNode(listemp.get(i).getSalaire()));
 employee.appendChild(salaire);
    }

 // create the xml file
 //transform the DOM Object to an XML File
 TransformerFactory transformerFactory = TransformerFactory.newInstance();
 Transformer transformer = transformerFactory.newTransformer();
 DOMSource domSource = new DOMSource(document);
 StreamResult streamResult = new StreamResult(new File(xmlFilePath));

 // If you use
 // StreamResult result = new StreamResult(System.out);
 // the output will be pushed to the standard output ...
 // You can use that for debugging

 transformer.transform(domSource, streamResult);

 System.out.println("Done creating XML File");

 } catch (ParserConfigurationException pce) {
 pce.printStackTrace();
 } catch (TransformerException tfe) {
 tfe.printStackTrace();
 }
}
}
  
