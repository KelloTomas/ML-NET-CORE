using System;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;

namespace MLCore.Migrations
{
    public partial class InitialCreate : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Trains",
                columns: table => new
                {
                    Id = table.Column<int>(nullable: false)
                        .Annotation("SqlServer:ValueGenerationStrategy", SqlServerValueGenerationStrategy.IdentityColumn),
                    Bod1Cis = table.Column<int>(nullable: false),
                    Bod1Naz = table.Column<string>(nullable: true),
                    Bod2Cis = table.Column<int>(nullable: false),
                    Bod2Naz = table.Column<string>(nullable: true),
                    VlakId = table.Column<int>(nullable: false),
                    Vlak = table.Column<int>(nullable: false),
                    Druh = table.Column<string>(nullable: true),
                    Loko = table.Column<string>(nullable: true),
                    Hmot = table.Column<int>(nullable: false),
                    Dlzka = table.Column<int>(nullable: false),
                    PocNaprav = table.Column<int>(nullable: false),
                    PocVoznov = table.Column<int>(nullable: false),
                    StrojveduciCislo = table.Column<string>(nullable: true),
                    GvdOdch = table.Column<DateTime>(nullable: true),
                    GvdPrich = table.Column<DateTime>(nullable: true),
                    GvdCasCesty = table.Column<int>(nullable: true),
                    Odch = table.Column<DateTime>(nullable: true),
                    Prich = table.Column<DateTime>(nullable: true),
                    CasCesty = table.Column<int>(nullable: true),
                    MeskanieOdchod = table.Column<int>(nullable: true),
                    MeskaniePrichod = table.Column<int>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Trains", x => x.Id);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Trains");
        }
    }
}
