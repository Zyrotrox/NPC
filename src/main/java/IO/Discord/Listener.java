package IO.Discord;

import IO.IListener;
import org.javacord.api.DiscordApi;
import org.javacord.api.DiscordApiBuilder;


public class Listener implements IListener {
    private DiscordApi api;
    private static String token = "MjY1NTUyMDY4NzM4MDIzNDI1.DrzIaQ.OAiIW1GMoFgWEga__NVXHiVNwxY";

    public Listener(){
        this.api = new DiscordApiBuilder().setToken(this.token).login().join();

        this.api.addMessageCreateListener(event -> onMessageReceived(event.getMessageContent()));
    }

    @Override
    public void onMessageReceived(String msg) {

    }
}
