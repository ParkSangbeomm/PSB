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

/*
//파일 이름 받아서 열기
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Main {
  public static void main(String[] args) {
    System.out.print("Enter file name: ");
    Scanner keyboard = new Scanner(System.in);
    String fileName = keyboard.next();
    Scanner inputStream = null;
    System.out.println("The file " + fileName + "\n" + "contains the following lines:");
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

/*
//csv파일 읽어와서 파일 만들기
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;
import java.util.Scanner;

public class Main {
  public static void main(String[] args){
    String fileName = "Transactions.txt";
    try{
      Scanner inputStream = new Scanner(new File(fileName));
      String line = inputStream.nextLine();
      double total = 0;
      while (inputStream.hasNextLine()){
        line = inputStream.nextLine(); // read one line
        String[] ary = line.split(","); // split words
        String SKU = ary[0];
        int quantity = Integer.parseInt(ary[1]);
        double price = Double.parseDouble(ary[2]);
        String description = ary[3];
        System.out.printf("Sold %d of %s (SKU: %s) at "+"$%1.2f each.\n", quantity, description, SKU, price);
        total += quantity * price;
      }
      System.out.printf("Total sales: $%1.2f\n",total);
      inputStream.close( );
    }
    //catch(IOException e) {System.out.println("Problem!");}
    catch(FileNotFoundException e) {System.out.println("Problem!");}
    
  }
}
*/

/*
//dat파일에다가 binary형식으로 
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    String fileName = "numbers.dat";
    try{
      ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(fileName));
      Scanner keyboard = new Scanner(System.in);
      System.out.println("Enter nonnegative integers.");
      System.out.println("Place a negative number at the " + "end.");
      int anInteger;
      do{
        anInteger = keyboard.nextInt();
        outputStream.writeInt(anInteger);
      } while (anInteger >= 0);
      System.out.println("Numbers and sentinel value");
      System.out.println("written to the file " + fileName);
      outputStream.close();
    }
    catch(FileNotFoundException e){
      System.out.println("Problem opening the file " + fileName);
    }
    catch(IOException e){
      System.out.println("Problem with output to file " + fileName);
    }
  }
}
*/
