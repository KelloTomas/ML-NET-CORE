using System;
using System.Collections.Generic;
using System.Text;

namespace MLCore
{
	interface IModel
	{
		void Init();
		void Train();
		void Evaluate();
		void Output();
	}
}
