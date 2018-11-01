package Info;

import Entities.Topic;
import Entities.Topics;

public class TopicDecipher {
    private Topics allTopics;

    public TopicDecipher(Topics allTopics){
        this.allTopics = allTopics;
    }

    public Topics decipher(String str){
        Topics topics = new Topics();
        str = str.toUpperCase();
        for(Topic t : allTopics){
            for(String key : t.getKeywords()){
                if(str.contains(key.toUpperCase())){
                    topics.add(t);
                    break;
                }
            }
        }

        return topics;
    }

    public Topics getAllTopics() {
        return allTopics;
    }

    public void setAllTopics(Topics allTopics) {
        this.allTopics = allTopics;
    }
}
