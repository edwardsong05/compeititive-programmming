import java.util.Scanner;

/**
 * for the "Homework" problem on kattis
 * using a dynamic programming strategy 
 * https://open.kattis.com/problems/homework
 * 
 * note: the reason why I did this in java was because python kept giving me a problem
 */
public class Homework 
{
	private static String s;
	private static String s1;
	private static String s2;
	private static int[][] arr;
	
	public static void checkRightDown (int x, int y)
	{
		if (arr[s2.length()][s1.length()] != 1) // solution has not been found
		{
			if (x < s1.length() && arr[y][x+1] != 1) // we can check right
			{
				if (s1.charAt(x) == s.charAt(x+y)) // we have a match
				{
					arr[y][x+1] = 1;
					checkRightDown(x+1, y);
				}
			}
			
			if (y < s2.length() && arr[y+1][x] != 1) // we can check down
			{
				if (s2.charAt(y) == s.charAt(x+y)) // we have a match
				{
					arr[y+1][x] = 1;
					checkRightDown(x, y+1);
				}
			}
		}
	}
	
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		s = sc.nextLine();
		s1 = sc.nextLine();
		s2 = sc.nextLine();
		sc.close();
		
		arr = new int[s2.length()+1][];
		
		for (int i = 0; i < arr.length; i++)
		{
			arr[i] = new int[s1.length()+1];
		}
		
		checkRightDown(0, 0);
		
		if (arr[s2.length()][s1.length()] == 1)
		{
			System.out.println("yes");
		}
		else
		{
			System.out.println("no");
		}
	}
}
