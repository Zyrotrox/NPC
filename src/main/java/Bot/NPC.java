package Bot;

import Entities.Topic;
import Entities.Topics;
import IO.IListener;
import Info.TopicDecipher;

public class NPC {
    private IListener listener;
    private Topics topics;
    private TopicDecipher decipher;

    public NPC(){
        TopicFactory tf = new TopicFactory();
        this.topics = tf.readTopics();
        this.decipher = new TopicDecipher(this.topics);

        this.listener = new IO.Discord.Listener(){
            @Override
            public String onMessageReceived(String msg) {
                String res = "";
                System.out.println("MESSAGE RECEIVED: " + msg);
                for (Topic t : decipher.decipher(msg)) {
                    System.out.println("tat");
                    res += t.getName() + ", ";
                }

                return res;
            }
        };
    }
}
