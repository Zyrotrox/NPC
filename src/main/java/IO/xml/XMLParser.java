package IO.xml;

import Entities.Topic;
import Entities.Topics;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;

public class XMLParser {

    /*public Topics readTopics(){
        Topics topics = new Topics();
        Topic t;

        try {
            File inFile = new File(getClass().getResource("Topics.xml").getFile());

            DocumentBuilderFactory dbfactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbfactory.newDocumentBuilder();
            Document doc = dBuilder.parse(inFile);
            NodeList nList = doc.getElementsByTagName("Topic");

            for(int i = 0; i < nList.getLength(); i++){
                t = new Topic();

            }
        }catch (Exception e){

        }
        return topics;
    }*/
}
