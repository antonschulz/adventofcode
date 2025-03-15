import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Comparator;

public class Solution {

    public static class ParsedContent {
        private final Map<Integer, List<Integer>> pageOrderings;
        private final List<List<Integer>> updates;

        public ParsedContent(Map<Integer, List<Integer>> pageOrderings, List<List<Integer>> updates) {
            this.pageOrderings = pageOrderings;
            this.updates = updates;
        }

        public Map<Integer, List<Integer>> getPageOrderings() {
            return pageOrderings;
        }

        public List<List<Integer>> getUpdates() {
            return updates;
        }
    }

    public static void main(String[] args) {
        // Read the input file (relative to the class location)
        String content = FileReaderUtil.readInput("input.txt");
        if (content == null) {
            System.err.println("Failed to load input.");
            return;
        }

        // Process the content and get the parsed result.
        ParsedContent parsedData = processContent(content);
        if (parsedData == null) {
            System.err.println("Error processing content.");
            return;
        }

        // Use the returned content.
        System.out.println("Page Orderings:");
        for (Map.Entry<Integer, List<Integer>> entry : parsedData.getPageOrderings().entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }

        System.out.println("\nUpdates:");
        for (List<Integer> update : parsedData.getUpdates()) {
            System.out.println(update);
        }

        solvePartOne(parsedData);
        solvePartTwo(parsedData);
    }

    private static void solvePartOne(ParsedContent parsedData) {
        List<Integer> middleNumbers = new ArrayList<>();
        Integer updateLength;

        for (List<Integer> update : parsedData.getUpdates()) {
            updateLength = update.size();
            boolean valid = true;
            for (int i = 0; i < updateLength - 1; i++) {
                if (!valid) {
                    break;
                }
                Integer currentNumber = update.get(i);
                for (int j = i + 1; j < updateLength; j++) {
                    Integer numAfterwards = update.get(j);
                    // System.out.println("currentNumber: " + currentNumber + " numAfterwards: " +
                    // numAfterwards);
                    List<Integer> shouldBeAfterJ = parsedData.getPageOrderings().get(numAfterwards);
                    if (shouldBeAfterJ != null && shouldBeAfterJ.contains(currentNumber)) {
                        System.out.println("False Update: " + update);
                        valid = false;
                        break;
                    }
                }
            }
            if (valid) {
                Integer middle = update.get((update.size() / 2));
                System.out.println("COrrect update: " + update + " middleNum: " + middle);
                middleNumbers.add(middle);
            }
        }
        Integer sum = 0;
        for (Integer num : middleNumbers) {
            sum += num;
        }
        System.out.println(sum);
    }

    private static void solvePartTwo(ParsedContent parsedData) {
        List<List<Integer>> invalidUpdates = new ArrayList<>();
        Integer updateLength;

        for (List<Integer> update : parsedData.getUpdates()) {
            updateLength = update.size();
            boolean valid = true;
            for (int i = 0; i < updateLength - 1; i++) {
                if (!valid) {
                    break;
                }
                Integer currentNumber = update.get(i);
                for (int j = i + 1; j < updateLength; j++) {
                    Integer numAfterwards = update.get(j);
                    // System.out.println("currentNumber: " + currentNumber + " numAfterwards: " +
                    // numAfterwards);
                    List<Integer> shouldBeAfterJ = parsedData.getPageOrderings().get(numAfterwards);
                    if (shouldBeAfterJ != null && shouldBeAfterJ.contains(currentNumber)) {
                        System.out.println("False Update: " + update);
                        valid = false;
                        break;
                    }
                }
            }
            if (!valid) {
                invalidUpdates.add(update);
            }
        }
        class SortByPageOrdering implements Comparator<Integer> {
            public int compare(Integer a, Integer b) {
                List<Integer> afterA = parsedData.getPageOrderings().get(a);
                List<Integer> afterB = parsedData.getPageOrderings().get(b);
                if (afterA != null && afterA.contains(b)) {
                    return -1;
                }
                if (afterB != null && afterB.contains(a)) {
                    return 1;
                } else {
                    return 0;
                }
            }
        }
        int sum = 0;
        for (List<Integer> update : invalidUpdates) {
            Collections.sort(update, new SortByPageOrdering());
            Integer middle = update.get((update.size() / 2));
            sum += middle;
        }
        System.out.println("Part2: " + sum);
    }

    /**
     * Processes the input content by dividing it into page orderings and updates.
     * It returns a ParsedContent object containing both data structures.
     *
     * @param content the complete file content as a String.
     * @return a ParsedContent instance with the page orderings and updates.
     */
    private static ParsedContent processContent(String content) {
        // Split the content into two sections based on a blank line.
        String[] parts = content.split("\\r?\\n\\r?\\n");
        if (parts.length < 2) {
            System.err.println("The input does not contain both page orderings and updates.");
            return null;
        }

        String pageOrderingsStr = parts[0];
        String updatesStr = parts[1];

        // Process page orderings into a Map<Integer, List<Integer>>
        Map<Integer, List<Integer>> pageOrderings = new HashMap<>();
        String[] pageLines = pageOrderingsStr.split("\\r?\\n");
        for (String line : pageLines) {
            // Each line is expected to be in the format "number|number"
            String[] tokens = line.split("\\|");
            if (tokens.length != 2)
                continue;
            int key = Integer.parseInt(tokens[0].trim());
            int value = Integer.parseInt(tokens[1].trim());
            pageOrderings.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
        }

        // Process updates into a List<List<Integer>>
        List<List<Integer>> updates = new ArrayList<>();
        String[] updateLines = updatesStr.split("\\r?\\n");
        for (String line : updateLines) {
            // Each update line is expected to be in the format "num,num,num,..."
            String[] tokens = line.split(",");
            List<Integer> updateList = new ArrayList<>();
            for (String token : tokens) {
                updateList.add(Integer.parseInt(token.trim()));
            }
            updates.add(updateList);
        }

        return new ParsedContent(pageOrderings, updates);
    }
}

/**
 * Helper class to read file input from the classpath.
 */
class FileReaderUtil {
    /**
     * Reads the file from the classpath and returns its content as a String.
     *
     * @param fileName the name of the file to load (relative to the class location)
     * @return the file content as a String, or null if an error occurs.
     */
    public static String readInput(String fileName) {
        StringBuilder contentBuilder = new StringBuilder();
        try (InputStream is = FileReaderUtil.class.getResourceAsStream(fileName)) {
            if (is == null) {
                System.err.println("File not found: " + fileName);
                return null;
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(is))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    contentBuilder.append(line).append("\n");
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            return null;
        }
        return contentBuilder.toString();
    }
}