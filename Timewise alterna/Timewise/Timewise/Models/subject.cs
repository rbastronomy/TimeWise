namespace Timewise.Models
{
    public class subject
    {
        public subject() { }

        private string Name { get; set; }
        private int Id { get; set; }
        private string Parallel { get; set; }
        private int Semester { get; set; }
        private int Credits { get; set; }
        private int Lecturehours { get; set; }
        private int Lectureminutes { get; set; }
        private string Modality { get; set; }
        private int Total { get; set; }
        private teacher Teacher { get; set; }
    }
}
