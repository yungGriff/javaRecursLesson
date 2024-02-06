public class Main
{
	public static void main(String[] args) {
        int n = 10; // Change this value to generate Fibonacci sequence up to a different term
        System.out.println("Fibonacci sequence up to term " + n + ": " + generateFibonacci(n));
    }

    // Method to generate Fibonacci sequence up to the nth term
    public static String generateFibonacci(int n) {
        if (n <= 0) {
            return "Invalid input. Please provide a positive integer.";
        }

        StringBuilder result = new StringBuilder();
        int firstTerm = 1;
        int secondTerm = 1;

        // Display the first two terms
        result.append(firstTerm).append(", ").append(secondTerm);

        // Generate the Fibonacci sequence up to the nth term
        for (int i = 0; i < n; i++) {
            int nextTerm = firstTerm + secondTerm;
            result.append(", ").append(nextTerm);
            firstTerm = secondTerm;
            secondTerm = nextTerm;
        }

        return result.toString();
    }
}

