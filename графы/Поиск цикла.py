import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] adjMatrix;
    static boolean[] visited;
    static int[] parent;
    static List<Integer> cycle;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(reader.readLine());
        adjMatrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] parts = reader.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                adjMatrix[i][j] = Integer.parseInt(parts[j]);
            }
        }

        visited = new boolean[n];
        parent = new int[n];
        cycle = new ArrayList<>();

        Arrays.fill(parent, -1);

        boolean hasCycle = false;
        for (int i = 0; i < n && !hasCycle; i++) {
            if (!visited[i]) {
                if (dfs(i, -1)) {
                    hasCycle = true;
                }
            }
        }

        if (!hasCycle) {
            writer.write("NO\n");
        } else {
            writer.write("YES\n");
            writer.write(cycle.size() + "\n");
            for (int node : cycle) {
                writer.write((node + 1) + " ");
            }
            writer.write("\n");
        }

        reader.close();
        writer.close();
    }

    static boolean dfs(int v, int p) {
        visited[v] = true;
        parent[v] = p;

        for (int u = 0; u < n; u++) {
            if (adjMatrix[v][u] == 1) {
                if (!visited[u]) {
                    if (dfs(u, v)) {
                        return true;
                    }
                } else if (u != p) {
                    // Найден цикл
                    int current = v;
                    while (current != u && current != -1) {
                        cycle.add(current);
                        current = parent[current];
                    }
                    if (current != -1) {
                        cycle.add(u);
                        Collections.reverse(cycle);
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
