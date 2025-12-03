import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Day08 {
    public static void main(String[] args) {
        ArrayList<String> fileData = getFileData("src/InputFile");
        HashMap<String, ArrayList<int[]>> coords = new HashMap<>();
        ArrayList<String> antiNodes = new ArrayList<>();
        // Gets the coordinates of all the antennas and creates a blank map for the antinodes
        for (int y = 0; y < fileData.size(); y++){
            String row = "";
            for (int x = 0; x < fileData.get(y).length(); x++){
                row += ".";
                String currChar = String.valueOf(fileData.get(y).charAt(x));
                if (!currChar.equals(".")){
                    int[] currCoords = {x, y};
                    if (coords.get(currChar) == null){
                        ArrayList<int[]> list = new ArrayList<>();
                        list.add(currCoords);
                        coords.put(currChar, list);
                    }
                    else{
                        coords.get(currChar).add(currCoords);
                    }
                }
            }
            antiNodes.add(row);
        }

        int partOneAnswer = 0;
        int partTwoAnswer = 0;
        int maxY = fileData.size();
        int maxX = fileData.getFirst().length();
        ArrayList<String> part2AntiNodes = (ArrayList<String>) antiNodes.clone();

        // marks where all the antinodes will be
        for (String freq : coords.keySet()){
            ArrayList<int[]> list = coords.get(freq);
            for (int i = 0; i < list.size(); i++){
                int nodeX = list.get(i)[0];
                int nodeY = list.get(i)[1];
                for (int j = 0; j < list.size(); j++){
                    // prevents the nodes from detecting themselves
                    if (i != j){
                        int diffX = nodeX - list.get(j)[0];
                        int diffY = nodeY - list.get(j)[1];
                        int antiNodeX = nodeX + diffX;
                        int antiNodeY = nodeY + diffY;
                        boolean inBounds = antiNodeX < maxX && antiNodeX >= 0 && antiNodeY < maxY && antiNodeY >= 0;
                        if (inBounds){
                            antiNodes.set(antiNodeY, antiNodes.get(antiNodeY).substring(0, antiNodeX) + "#" + antiNodes.get(antiNodeY).substring(antiNodeX + 1));
                        }
                        // continues to add antinodes until out of bounds
                        while (inBounds){
                            part2AntiNodes.set(antiNodeY, part2AntiNodes.get(antiNodeY).substring(0, antiNodeX) + "#" + part2AntiNodes.get(antiNodeY).substring(antiNodeX + 1));
                            antiNodeX += diffX;
                            antiNodeY += diffY;
                            inBounds = (antiNodeX < maxX && antiNodeX >= 0 && antiNodeY < maxY && antiNodeY >= 0);
                        }
                    }
                }
                part2AntiNodes.set(nodeY, part2AntiNodes.get(nodeY).substring(0, nodeX) + "#" + part2AntiNodes.get(nodeY).substring(nodeX + 1));
            }
        }

        for (String row : antiNodes){
            for (int i = 0; i < row.length(); i++){
                if (row.charAt(i) == '#'){
                    partOneAnswer++;
                }
            }
        }

        for (String row : part2AntiNodes){
            for (int i = 0; i < row.length(); i++){
                if (row.charAt(i) == '#'){
                    partTwoAnswer++;
                }
            }
        }

        System.out.println("Part 1: " + partOneAnswer);
        System.out.println("Part 2: " + partTwoAnswer);
    }
    public static ArrayList<String> getFileData(String fileName) {
        ArrayList<String> fileData = new ArrayList<String>();
        try {
            File f = new File(fileName);
            Scanner s = new Scanner(f);
            while (s.hasNextLine()) {
                String line = s.nextLine();
                if (!line.equals(""))
                    fileData.add(line);
            }
            return fileData;
        }
        catch (FileNotFoundException e) {
            return fileData;
        }
    }
}
