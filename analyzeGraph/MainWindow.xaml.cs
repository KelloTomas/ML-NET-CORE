using System;
using System.Collections.Generic;
using System.Windows;
using System.Windows.Media;
using System.Windows.Shapes;

namespace analyzeGraph
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	public partial class MainWindow : Window
	{
		public MainWindow()
		{
			InitializeComponent();
		}
		protected override void OnContentRendered(EventArgs e)
		{
			base.OnContentRendered(e);
			List<Tuple<SolidColorBrush, List<double>>> data = new List<Tuple<SolidColorBrush, List<double>>>
			{
				new Tuple<SolidColorBrush, List<double>>(Brushes.Red, new List<double>
				{
					10,5,2,6,8,5,2,4,8,5,8,9,6,8
				}),
				new Tuple<SolidColorBrush, List<double>>(Brushes.Red, new List<double>
				{
					1,10,5
				}),
				new Tuple<SolidColorBrush, List<double>>(Brushes.Red, new List<double>
				{
					2,1,10
				}),
				new Tuple<SolidColorBrush, List<double>>(Brushes.Blue, new List<double>
				{
					2,3,5
				}),
				new Tuple<SolidColorBrush, List<double>>(Brushes.Green, new List<double>
				{
					1,5,4
				}),
			};
			ShowData(10, data);
		}
		public void ShowData(double yMax, List<Tuple<SolidColorBrush, List<double>>> data)
		{
			const double _margin = 10;
			double _xMin = _margin;
			double _xMax = canGraph.Width - _margin;
			double _yMax = canGraph.Height - _margin;
			const double _step = 10;

			// Make the X axis.
			GeometryGroup xaxis_geom = new GeometryGroup();
			xaxis_geom.Children.Add(new LineGeometry(
				new Point(0, _yMax), new Point(canGraph.Width, _yMax)));
			for (double x = _xMin + _step;
				x <= canGraph.Width - _step; x += _step)
			{
				xaxis_geom.Children.Add(new LineGeometry(
					new Point(x, _yMax - _margin / 2),
					new Point(x, _yMax + _margin / 2)));
			}

			Path xaxis_path = new Path();
			xaxis_path.StrokeThickness = 1;
			xaxis_path.Stroke = Brushes.Black;
			xaxis_path.Data = xaxis_geom;

			canGraph.Children.Add(xaxis_path);

			// Make the Y ayis.
			GeometryGroup yaxis_geom = new GeometryGroup();
			yaxis_geom.Children.Add(new LineGeometry(
				new Point(_xMin, 0), new Point(_xMin, canGraph.Height)));
			for (double y = _step; y <= canGraph.Height - _step; y += _step)
			{
				yaxis_geom.Children.Add(new LineGeometry(
					new Point(_xMin - _margin / 2, y),
					new Point(_xMin + _margin / 2, y)));
			}

			Path yaxis_path = new Path();
			yaxis_path.StrokeThickness = 1;
			yaxis_path.Stroke = Brushes.Black;
			yaxis_path.Data = yaxis_geom;

			canGraph.Children.Add(yaxis_path);

			foreach (var d in data)
			{
				PointCollection points = new PointCollection();
				double x = 0;
				foreach(var y in d.Item2)
				{
					points.Add(new Point(x++*_xMax/(d.Item2.Count-1), y/yMax*_yMax));
				}

				Polyline polyline = new Polyline();
				polyline.StrokeThickness = 1;
				polyline.Stroke = d.Item1;
				polyline.Points = points;

				canGraph.Children.Add(polyline);
			}
		}
	}
}
