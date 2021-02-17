import com.aldebaran.qi.Application;
import com.aldebaran.qi.helper.proxies.ALTextToSpeech;

public class HelloWorld {

    public static void main(String[] args) throws Exception {
        NAO nao = new NAO();
        nao.connect("localhost", 1234);
        nao.say("Hello world!");
    }
}