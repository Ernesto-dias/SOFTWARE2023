class Main {

  public static void main(String[] args) {
    System.out.println("Inicializando....");
    System.out.println("Car....");
    Car car = new Car("AMQ123", new Account("Andrez Loiza","AND1235","andres@hotmail.com","12365"));
    car.passenger = 4;
    car.printDataCar();

    System.out.println("Uberx....");
    UberX uberx = new UberX ("MkL185", new Account("Maria Loyola", "JKL12365","maria@hotmail.com", "125378"),"Toyota","Corolla");
  }
}