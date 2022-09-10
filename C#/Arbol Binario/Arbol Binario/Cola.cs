using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arbol_Binario
{
    public class Cola<T>
    {
        private List<T> datos = new List<T>();

        public void encolar(T elemento)
        {
            this.datos.Add(elemento);
        }

        public T desencolar()
        {
            T elementoTemporal = this.datos[0];
            this.datos.RemoveAt(0);
            return elementoTemporal;
        }

        public T tope()
        {
            return this.datos[0];
        }

        public bool esVacia()
        {
            if (this.datos.Count == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
