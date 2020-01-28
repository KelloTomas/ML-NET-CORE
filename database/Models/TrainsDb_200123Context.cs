using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace Database.Models
{
    public partial class TrainsDb_200123Context : DbContext
    {
        public TrainsDb_200123Context()
        {
        }

        public TrainsDb_200123Context(DbContextOptions<TrainsDb_200123Context> options)
            : base(options)
        {
        }

        public virtual DbSet<CzPreosGtn> CzPreosGtn { get; set; }
        public virtual DbSet<CzPreosPreos> CzPreosPreos { get; set; }
        public virtual DbSet<CzTreko> CzTreko { get; set; }
        public virtual DbSet<CzVelib> CzVelib { get; set; }
        public virtual DbSet<SkBb> SkBb { get; set; }
        public virtual DbSet<SkCaMySql> SkCaMySql { get; set; }
        public virtual DbSet<SkCaOracle> SkCaOracle { get; set; }
        public virtual DbSet<SkKrasnoNkysMySql> SkKrasnoNkysMySql { get; set; }
        public virtual DbSet<SkKrasnoNkysOracle> SkKrasnoNkysOracle { get; set; }
        public virtual DbSet<SkKutyMySql> SkKutyMySql { get; set; }
        public virtual DbSet<SkKutyOracle> SkKutyOracle { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. See http://go.microsoft.com/fwlink/?LinkId=723263 for guidance on storing connection strings.
                optionsBuilder.UseSqlServer("Server=dokelu.kst.fri.uniza.sk;Database=TrainsDb_20-01-23;User Id=kello4;password=kello4;Trusted_Connection=False;");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.HasAnnotation("ProductVersion", "2.2.4-servicing-10062");

            modelBuilder.Entity<CzPreosGtn>(entity =>
            {
                entity.ToTable("CZ-PREOS_GTN");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<CzPreosPreos>(entity =>
            {
                entity.ToTable("CZ-PREOS_PREOS");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<CzTreko>(entity =>
            {
                entity.ToTable("CZ-TREKO");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<CzVelib>(entity =>
            {
                entity.ToTable("CZ-VELIB");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<SkBb>(entity =>
            {
                entity.ToTable("SK-BB");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<SkCaMySql>(entity =>
            {
                entity.ToTable("SK-CA-MySQL");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<SkCaOracle>(entity =>
            {
                entity.ToTable("SK-CA-Oracle");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<SkKrasnoNkysMySql>(entity =>
            {
                entity.ToTable("SK-KrasnoNKys-MySQL");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<SkKrasnoNkysOracle>(entity =>
            {
                entity.ToTable("SK-KrasnoNKys-Oracle");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<SkKutyMySql>(entity =>
            {
                entity.ToTable("SK-Kuty-MySQL");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });

            modelBuilder.Entity<SkKutyOracle>(entity =>
            {
                entity.ToTable("SK-Kuty-Oracle");

                entity.Property(e => e.ArrIls).HasColumnName("ArrILS");

                entity.Property(e => e.Delay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.DepIls).HasColumnName("DepILS");

                entity.Property(e => e.FromSr70).HasColumnName("FromSR70");

                entity.Property(e => e.LengthSect).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredDelay).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredLength).HasColumnType("numeric(18, 0)");

                entity.Property(e => e.PredSr70)
                    .HasColumnName("PredSR70")
                    .HasColumnType("numeric(18, 0)");

                entity.Property(e => e.ToSr70).HasColumnName("ToSR70");
            });
        }
    }
}
