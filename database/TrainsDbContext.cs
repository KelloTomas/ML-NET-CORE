using Microsoft.EntityFrameworkCore;
using System;

namespace Database
{
    public partial class TrainsDbContext : DbContext
    {
        public TrainsDbContext()
        {
        }

        public TrainsDbContext(DbContextOptions<TrainsDbContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Trains> Trains { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. See http://go.microsoft.com/fwlink/?LinkId=723263 for guidance on storing connection strings.
                optionsBuilder.UseSqlServer("Server=dokelu.kst.fri.uniza.sk;Database=TrainsDbCopy;Trusted_Connection=False;User Id=kello4;Password=kello4;");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.HasAnnotation("ProductVersion", "2.2.2-servicing-10034");
        }
    }
}
