package IO.Discord;

import IO.IListener;
import org.javacord.api.DiscordApi;
import org.javacord.api.DiscordApiBuilder;


public class Listener implements IListener {
    private DiscordApi api;
    private static String token = "MjY1NTUyMDY4NzM4MDIzNDI1.DrzIaQ.OAiIW1GMoFgWEga__NVXHiVNwxY";

    public Listener(){
        this.api = new DiscordApiBuilder().setToken(this.token).login().join();

        this.api.addMessageCreateListener(event -> event.getChannel().sendMessage(onMessageReceived(event.getMessageContent())));
    }

    @Override
    public String onMessageReceived(String msg) {
        String response = "";

        System.out.println("MESSAGE RECEIVED! " + msg);

        if(msg.equalsIgnoreCase("!ping")){
            response = "Pong!";
        }
        //todo

        return response;
    }
}
