package Bot;

import Entities.Messages;
import Entities.Topics;
import IO.IListener;

public class NPC {
    private IListener listener;
    private Topics topics;

    public NPC(){
        this.listener = new IO.Discord.Listener();
    }
}
