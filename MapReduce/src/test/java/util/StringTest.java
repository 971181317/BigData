package util;

import org.junit.Test;

import java.util.StringTokenizer;

public class StringTest {
    @Test
    public void split() {
        String[] split = StringUtil.split(",,");
//        String[] split = "Name\tPlatform\tYear_of_Release\tGenre\tPublisher\tNA_Sales\tEU_Sales\tJP_Sales\tOther_Sales\tGlobal_Sales\tCritic_Score\tCritic_Count\tUser_Score\tUser_Count\tDeveloper\tRating\n".split("\t");
//        String[] split = "Minna de Jibun no Setsumeisho: B-Kata_ A-Kata_ AB-Kata_ O-Kata,DS,2008,Misc,GungHo,0,0,0.04,0,0.04,,,,,,".split(",");
        for (String s : split) {
            System.out.println("," + s);
        }
    }

    @Test
    public void split2() {
        StringTokenizer st = new StringTokenizer(",,,", ",");
        while (st.hasMoreElements()) {
            System.out.println("st " + st.nextElement());
        }
    }
}
