namespace Timewise
{
    public partial class Menu : Form
    {
        public Menu()
        {
            Text = "Proyecto TimeWise";
            Size = new Size(800, 600);
            InitializeComponent();

        }
        private void button1_Click(object sender, EventArgs e)
        {
            //MessageBox.Show("¡Botón Opción 1 funciona correctamente!");
            Horario opcionHorario = new Horario();
            opcionHorario.StartPosition = FormStartPosition.Manual;
            opcionHorario.Location = this.Location;
            this.Hide();
            opcionHorario.ShowDialog();
        }
        private void button2_Click(object sender, EventArgs e)
        {
            /*Horario form1 = new Horario();
            form1.Show();*/
        }
        private void button3_Click(object sender, EventArgs e)
        {
            /*Horario form1 = new Horario();
            form1.Show();*/
        }
        private void button4_Click(object sender, EventArgs e)
        {
            Close();
            /*Horario form1 = new Horario();
            form1.Show();*/
        }
    }
}
