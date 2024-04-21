using System;

namespace crescente
{
	class Program
	{
		static void Main(string[] args)
		{
			int x, y;

			Console.WriteLine("Digite dois números:");
			x = int.Parse(Console.ReadLine());
			y = int.Parse(Console.ReadLine());

			while (x != y)
			{
				if (x > y)
				{
					Console.WriteLine("DECRESCENTE!");
				}
				else
				{
					Console.WriteLine("CRESCENTE!");
				}

				Console.WriteLine("Digite outros dois números:");
				x = int.Parse(Console.ReadLine());
				y = int.Parse(Console.ReadLine());
			}
		}
	}
}
