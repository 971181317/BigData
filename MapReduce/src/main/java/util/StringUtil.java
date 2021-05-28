package util;

import java.util.ArrayList;
import java.util.List;

public class StringUtil {
    public static String[] split(String line) {
        List<String> list = new ArrayList<>();
        int start = 0;
        int end = -1;
        while (true) {
            start = end + 1;
            end = line.indexOf(",", start);
            if (end < 0) {
                //最后了
                end = line.length();
            }
            String p1 = line.substring(start, end);
            list.add(p1);
            if (end >= line.length() - 1) {
                break;
            }
        }
        return list.toArray(new String[0]);
    }
}
