/*
//파일에 입력하기 라인별로
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String fileName = "out.txt";
    PrintWriter outputStream = null;
    try {
      outputStream = new PrintWriter(fileName);
    } catch (FileNotFoundException e) {
      System.out.println("Error opening the file" + fileName);
      System.exit(0);
    }
    System.out.println("Enter three lines of text:");
    Scanner keyboard = new Scanner(System.in);
    for (int count = 1; count <= 3; count++) {
      String line = keyboard.nextLine();
      outputStream.println(count + " " + line);
    }
    outputStream.close();
    System.out.println("Those lines were written to " + fileName);
  }
}
*/

/*
//라인별로 읽기
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Main {
  public static void main(String[] args) {
    String fileName = "out.txt";
    Scanner inputStream = null;
    System.out.println("The file " + fileName + "\ncontains the following lines:");
    try {
      inputStream = new Scanner(new File(fileName));
    } catch (FileNotFoundException e) {
      System.out.println("Error opening the file " + fileName);
      System.exit(0);
    }
    while (inputStream.hasNextLine()) {
      String line = inputStream.nextLine();
      System.out.println(line);
    }
    inputStream.close();
  }
}
*/
