using CsvHelper;
using ExcelDataReader;
using System.Data;

namespace Timewise.Models
{
    public static class Utilidades
    {
        public static DataTable CargarDatos()
        {
            DataTable Dt = new DataTable();

            OpenFileDialog Dialog = new OpenFileDialog();
            Dialog.Filter = "Archivos CSV (*.csv)|*.csv|Archivos XLSX (*.xlsx)|*.xlsx";
            DialogResult Result = Dialog.ShowDialog();
            if (Result != DialogResult.OK) return null;
            try
            {
                if (Dialog.FileName.EndsWith(".csv"))
                {
                    using (var Reader = new StreamReader(Dialog.FileName))
                    using (var Csv = new CsvReader(Reader, System.Globalization.CultureInfo.InvariantCulture))
                    {
                        Csv.Read();
                        Csv.ReadHeader();
                        foreach (var Header in Csv.HeaderRecord) Dt.Columns.Add(Header);
                        while (Csv.Read())
                        {
                            DataRow Fila = Dt.NewRow();
                            foreach (DataColumn Columna in Dt.Columns)
                                Fila[Columna.ColumnName] = Csv.GetField(Columna.DataType, Columna.ColumnName);
                            Dt.Rows.Add(Fila);
                        }
                    }
                }
                else if (Dialog.FileName.EndsWith(".xlsx"))
                {
                    using (var stream = File.Open(Dialog.FileName, FileMode.Open, FileAccess.Read))
                    {
                        var Reader = ExcelReaderFactory.CreateReader(stream);
                        var dataSet = Reader.AsDataSet(new ExcelDataSetConfiguration()
                        {
                            UseColumnDataType = true,
                            ConfigureDataTable = (tableReader) => new ExcelDataTableConfiguration()
                            {
                                UseHeaderRow = true
                            }
                        });
                        Dt = dataSet.Tables[0];
                    }
                }
            }
            catch (Exception Ex)
            {
                MessageBox.Show($"No se pudo cargar el archivo: {Ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return null;
            }
            return Dt;
        }
    }
}
