import com.aldebaran.qi.Application;
import com.aldebaran.qi.helper.proxies.ALTextToSpeech;

public class NAO {
    private String name;
    private Application app;

    public void connect(String hostname, int port) {
        String robotUrl = "tcp://" + hostname + ":" + port;
        // Create a new application
        this.app = new Application(new String[]{}, robotUrl);
        // Start your application
        this.app.start();
    }

    public void say(String text) throws Exception {
        // Create an ALTextToSpeech object and link it to your current session
        ALTextToSpeech tts = new ALTextToSpeech(this.app.session());
        // Make your robot say something
        tts.say("Hello World!");
    }
}
