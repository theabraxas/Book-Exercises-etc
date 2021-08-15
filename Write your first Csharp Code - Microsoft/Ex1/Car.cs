namespace Ex1
{
    public class Car {
        // Attributes
        public string Color {get; set; }
        public string Brand {get; set; }
        private int wheels;
        public int Wheels {
            get {return wheels; }
            set {wheels = value;}
        }
        // Constructors
        public Car(string color, string brand, int wheels)
        {
            Color = color;
            Brand = brand;
            Wheels = wheels;
        }

        // Methods
        public void ThisIsYourCar() {
            System.Console.WriteLine("My Car is:" + Color + " " + Wheels); 
        }

        public void MethodOne(int i) {
            Wheels = i;
        }

        public string MethodTwo(string name) {
            return name;
        }
    }
}