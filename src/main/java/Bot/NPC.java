package Bot;

import IO.IListener;

public class NPC {
    private IListener listener;

    public NPC(){
        this.listener = new IO.Discord.Listener();
    }
}
