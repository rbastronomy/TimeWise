using iTextSharp.text;
using iTextSharp.text.pdf;
using System.ComponentModel;
using System.Data;
using System.Diagnostics.Eventing.Reader;
using System.Reflection.Metadata;
using Timewise.Models;
using Document = iTextSharp.text.Document;

namespace Timewise
{
    public partial class Horario : Form
    {
        private System.Windows.Forms.Button btnCargarDatos;

        public Horario()
        {
            InitializeComponent();
            //btnCargarDatos.Click += button1_Click_1;
            btnCargarDatos = new System.Windows.Forms.Button();
        }
        private void Form1_Load_1(object sender, EventArgs e)
        {
            // Configurar las columnas de la tabla
            dataGridView1.Columns.Add("Hora", "Hora");
            dataGridView1.Columns.Add("Lunes", "Lunes");
            dataGridView1.Columns.Add("Martes", "Martes");
            dataGridView1.Columns.Add("Miércoles", "Miércoles");
            dataGridView1.Columns.Add("Jueves", "Jueves");
            dataGridView1.Columns.Add("Viernes", "Viernes");

            // Agregar filas a la tabla
            for (int i = 8; i <= 23; i++)
            {
                dataGridView1.Rows.Add(i + ":00", "", "", "", "", "");
            }

            // Ajustar el ancho de las columnas
            dataGridView1.AutoResizeColumns();
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e) { }

        private void button1_Click_1(object sender, EventArgs e)
        {
            DataTable datos = Utilidades.CargarDatos();
            if (datos != null)
            {
                dataGridView1.DataSource = datos;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //MessageBox.Show("¡Botón Opción 1 funciona correctamente!");
            Menu menureturn = new Menu();
            menureturn.StartPosition = FormStartPosition.Manual;
            menureturn.Location = this.Location;
            this.Hide();
            menureturn.ShowDialog();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SaveFileDialog saveDialog = new SaveFileDialog();
            saveDialog.Filter = "PDF files (*.pdf)|*.pdf|PNG files (*.png)|*.png|Excel files (*.xlsx)|*.xlsx";
            saveDialog.FilterIndex = 1;
            saveDialog.RestoreDirectory = true;

            if(saveDialog.ShowDialog() == DialogResult.OK)
            {
                string FileName = saveDialog.FileName;
                string extension = Path.GetExtension(FileName);

                if (extension == ".pdf") 
                {
                    if(FileName != "")
                    {
                        Document doc = new Document(iTextSharp.text.PageSize.A4.Rotate(), 10, 10, 10, 10);
                        PdfWriter writer = PdfWriter.GetInstance(doc, new FileStream(FileName, FileMode.Create));
                        doc.Open();
                        PdfPTable pdfTable = new PdfPTable(dataGridView1.ColumnCount);

                        //agregar encabezados
                        for (int i = 0; i < dataGridView1.Columns.Count; i++)
                            pdfTable.AddCell(new Phrase(dataGridView1.Columns[i].HeaderText));
                        pdfTable.HeaderRows = 1;
                        for(int i = 0; i < dataGridView1.Rows.Count; i++)
                        {
                            for(int j = 0; j < dataGridView1.Columns.Count; j++)
                            {
                                if (dataGridView1[j,i].Value != null)
                                {
                                    pdfTable.AddCell(new Phrase(dataGridView1[j,i].Value.ToString()));
                                }
                            }
                        }
                        doc.Add(pdfTable);
                        doc.Close();
                    }
                }
                else if (extension == ".png") 
                {
                    if (FileName != "")
                    {

                    }
                }
                else if (extension == ".xlsx") 
                {
                    if (FileName != "")
                    {

                    }
                }
                
            }
        }
    }
}