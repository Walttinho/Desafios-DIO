using System;

class Program
{
  static void Main(string[] args)
  {
    string registroEmail;
    string registroNome;
    string registroSenha;

    registroEmail = Console.ReadLine();
    registroNome = Console.ReadLine();
    registroSenha = Console.ReadLine();

    Console.WriteLine($"{registroNome}, verifique o email: {registroEmail} para ativar.");

  }
}
