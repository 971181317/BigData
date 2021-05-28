import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import util.StringUtil;

import java.io.IOException;

public class Sales {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        String[] otherArgs = (new GenericOptionsParser(conf, args)).getRemainingArgs();
        if (otherArgs.length < 2) {
            System.err.println("Usage: wordcount <in> [<in>...] <out>");
            System.exit(2);
        }
        Job job = Job.getInstance(conf, "Sales");        //设置环境参数
        job.setJarByClass(Sales.class);                //设置整个程序的类名
        job.setMapperClass(_Mapper.class); //添加Mapper类
        job.setReducerClass(_Reducer.class);  //添加Reducer类
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);
        job.setOutputKeyClass(Text.class);                    //设置输出类型
        job.setOutputValueClass(Text.class);             //设置输出类型
        for (int i = 0; i < otherArgs.length - 1; ++i) {
            FileInputFormat.addInputPath(job, new Path(otherArgs[i]));  //设置输入文件
        }
        FileOutputFormat.setOutputPath(job, new Path(otherArgs[otherArgs.length - 1]));//设置输出文件
        System.exit(job.waitForCompletion(true) ? 0 : 1);


    }

    public static class _Reducer extends Reducer<Text, Text, Text, Text> {
        public _Reducer() {
        }

        public void reduce(Text key, Iterable<Text> values, Reducer<Text, Text, Text, Text>.Context context) throws IOException, InterruptedException {
            if (key.toString().equals("name")) {
                //统计名称
                //合并所有名称为一行
                StringBuilder sb = new StringBuilder();
                for (Text v : values) {
                    //;分割每个结果
                    sb.append(v.toString()).append(";");
                }
                context.write(key, new Text(sb.toString()));
            } else {
                //统计数目
                int sum = 0;
                //统计分类的总数
                for (Text v : values) {
                    sum += Integer.parseInt(v.toString());
                }
                context.write(key, new Text(String.valueOf(sum)));
            }
        }
    }

    public static class _Mapper extends Mapper<Object, Text, Text, Text> {
        private final static Text one = new Text("1");

        public _Mapper() {
        }

        public void map(Object key, Text value, Mapper<Object, Text, Text, Text>.Context context) throws IOException, InterruptedException {
            //分割数组
            String[] arr = StringUtil.split(value.toString());
            //找到全球销售额，单位百万
            if (!arr[9].equals("")) {
                double sales = Double.parseDouble(arr[9]);
                if (sales <= 0.5) {
                    //小于等于50w
                    context.write(new Text("0.5"), one);
                } else if (sales <= 1) {
                    //小于等于100w
                    context.write(new Text("1"), one);
                } else if (sales <= 5) {
                    //小于等于500w
                    context.write(new Text("5"), one);
                } else if (sales <= 10) {
                    //小于等于1000w
                    context.write(new Text("10"), one);
                    //大于100w统计名称
                    context.write(new Text("name"), new Text(arr[0] + "," + sales));
                } else {
                    //大于1000w
                    context.write(new Text("10+"), one);
                    //大于100w统计名称
                    context.write(new Text("name"), new Text(arr[0] + "," + sales));
                }
            }
        }
    }
}
