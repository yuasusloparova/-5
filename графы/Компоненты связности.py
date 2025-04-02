import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static List<List<Integer>> components;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(reader.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(reader.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        visited = new boolean[N + 1];
        components = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                List<Integer> component = new ArrayList<>();
                dfs(i, component);
                components.add(component);
            }
        }

        writer.write(components.size() + "\n");
        for (List<Integer> component : components) {
            writer.write(component.size() + "\n");
            for (int node : component) {
                writer.write(node + " ");
            }
            writer.write("\n");
        }

        reader.close();
        writer.close();
    }

    static void dfs(int node, List<Integer> component) {
        visited[node] = true;
        component.add(node);
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, component);
            }
        }
    }
}
