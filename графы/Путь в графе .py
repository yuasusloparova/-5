import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int[][] adjMatrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            String[] parts = reader.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                adjMatrix[i][j] = Integer.parseInt(parts[j]);
            }
        }

        String[] se = reader.readLine().split(" ");
        int s = Integer.parseInt(se[0]) - 1;
        int e = Integer.parseInt(se[1]) - 1;

        if (s == e) {
            writer.write("0\n");
            reader.close();
            writer.close();
            return;
        }

        int[] parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = -1;
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        parent[s] = s;

        boolean found = false;
        while (!queue.isEmpty()) {
            int current = queue.poll();
            if (current == e) {
                found = true;
                break;
            }
            for (int neighbor = 0; neighbor < N; neighbor++) {
                if (adjMatrix[current][neighbor] == 1 && parent[neighbor] == -1) {
                    parent[neighbor] = current;
                    queue.add(neighbor);
                }
            }
        }

        if (!found) {
            writer.write("-1\n");
        } else {
            LinkedList<Integer> path = new LinkedList<>();
            int current = e;
            while (current != s) {
                path.addFirst(current + 1);
                current = parent[current];
            }
            path.addFirst(s + 1);

            writer.write((path.size() - 1) + "\n");
            for (int node : path) {
                writer.write(node + " ");
            }
            writer.write("\n");
        }

        reader.close();
        writer.close();
    }
}
