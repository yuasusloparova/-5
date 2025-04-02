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
        char[][] maze = new char[N][N];
        for (int i = 0; i < N; i++) {
            String line = reader.readLine();
            maze[i] = line.toCharArray();
        }

        String[] coordinates = reader.readLine().split(" ");
        int startRow = Integer.parseInt(coordinates[0]) - 1;
        int startCol = Integer.parseInt(coordinates[1]) - 1;

        if (maze[startRow][startCol] != '.') {
            writer.write("0\n");
            reader.close();
            writer.close();
            return;
        }

        int area = 0;
        boolean[][] visited = new boolean[N][N];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{startRow, startCol});
        visited[startRow][startCol] = true;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            area++;

            for (int i = 0; i < 4; i++) {
                int newRow = current[0] + dr[i];
                int newCol = current[1] + dc[i];

                if (newRow >= 0 && newRow < N && newCol >= 0 && newCol < N) {
                    if (maze[newRow][newCol] == '.' && !visited[newRow][newCol]) {
                        visited[newRow][newCol] = true;
                        queue.add(new int[]{newRow, newCol});
                    }
                }
            }
        }

        writer.write(area + "\n");
        reader.close();
        writer.close();
    }
}
