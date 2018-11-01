package Bot;

import Entities.Answer;
import Entities.Answers;
import Entities.Topic;
import Entities.Topics;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.util.ArrayList;

public class TopicFactory {

    public Topics readTopics(){
        Topics topics = new Topics();
        Topic t;
        ArrayList<String> keywords;

        try {

            Document doc = getDocument(new File(getClass().getClassLoader().getResource("Topics.xml").getFile()));
            NodeList nList = doc.getElementsByTagName("Topic");

            Element elem;
            Element keywordElem;
            NodeList keywordNodes;
            for(int i = 0; i < nList.getLength(); i++){
                keywords = new ArrayList<String>();
                if(nList.item(i).getNodeType() == Node.ELEMENT_NODE){
                    t = new Topic();
                    elem = (Element) nList.item(i);

                    keywordNodes = elem.getChildNodes();
                    for(int j = 0; j < keywordNodes.getLength(); j++){
                        if(keywordNodes.item(j).getNodeType() == Node.ELEMENT_NODE){
                            keywordElem = (Element) keywordNodes.item(j);
                            keywords.add(keywordElem.getAttribute("value"));
                        }
                    }
                    t.setId(Integer.parseInt(elem.getAttribute("id")));
                    t.setName(elem.getAttribute("name"));
                    t.setAnswers(readAnswers(t.getId()));
                    t.setKeywords(keywords);
                    topics.add(t);
                }

            }
        }catch (Exception e){
            System.out.println("error");
            e.printStackTrace();
        }
        return topics;
    }

    private Answers readAnswers(int topicId){
        Answers answers = new Answers();
        Answer a;

        try{
            Document doc = getDocument(new File(getClass().getClassLoader().getResource("Answers.xml").getFile()));
            NodeList nList = doc.getElementsByTagName("Answer");

            Element elem;
            Element answerElem;
            NodeList answerTopics;
            boolean onTopic = false;
            for(int i = 0; i < nList.getLength(); i++){
                if(nList.item(i).getNodeType() == Node.ELEMENT_NODE){
                    a = new Answer();
                    elem = (Element) nList.item(i);
                    answerTopics = elem.getChildNodes();
                    for(int j = 0; j < answerTopics.getLength(); j++){
                        if(answerTopics.item(j).getNodeType() == Node.ELEMENT_NODE){
                           answerElem = (Element) answerTopics.item(j);
                           if(Integer.parseInt(answerElem.getAttribute("id")) == topicId){  //right topic, copy
                               onTopic = true;
                               break;
                           }
                        }
                    }

                    if(onTopic){
                        a.setId(Integer.parseInt(elem.getAttribute("id")));
                        a.setStr(elem.getAttribute("str"));
                        answers.add(a);
                        onTopic = false;
                    }
                }
            }
        }catch (Exception e){
            System.out.println("error");
            e.printStackTrace();
        }
        return answers;
    }

    private Document getDocument(File inFile){
        try {
            DocumentBuilderFactory dbfactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbfactory.newDocumentBuilder();
            return dBuilder.parse(inFile);
        }catch (Exception e){
            System.out.println("error");
            e.printStackTrace();
            return null;
        }
    }
}
