using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Arbol_Binario;

namespace Arbol_Binario
{
    public class ArbolBinario<T>
    {
        private T dato;
        private ArbolBinario<T> hijoIzquierdo;
        private ArbolBinario<T> hijoDerecho;

        public ArbolBinario (T dato)
        {
            this.dato = dato;
        }

        public T getDatoRaiz()
        {
            return this.dato;
        }

        public ArbolBinario<T> getHijoIzquierdo()
        {
            return this.hijoIzquierdo;
        }

		public ArbolBinario<T> getHijoDerecho()
		{
			return this.hijoDerecho;
		}

		public void agregarHijoIzquierdo(ArbolBinario<T> hijo)
		{
			this.hijoIzquierdo = hijo;
		}

		public void agregarHijoDerecho(ArbolBinario<T> hijo)
		{
			this.hijoDerecho = hijo;
		}

		public void eliminarHijoIzquierdo()
		{
			this.hijoIzquierdo = null;
		}

		public void eliminarHijoDerecho()
		{
			this.hijoDerecho = null;
		}

		public bool esHoja()
		{
			return this.hijoIzquierdo == null && this.hijoDerecho == null;
		}

		public void inorden()
		{
			if (this.hijoIzquierdo != null)
            {
				this.hijoIzquierdo.inorden();
            }
			Console.WriteLine(this.dato);
			if (this.hijoDerecho != null)
            {
				this.hijoDerecho.inorden();
            }
		}

		public void preorden()
		{
			Console.WriteLine(this.dato);
			if (this.hijoIzquierdo != null)
			{
				this.hijoIzquierdo.preorden();
			}
			if (this.hijoDerecho != null)
			{
				this.hijoDerecho.preorden();
			}
		}

		public void postorden()
		{
			Console.WriteLine(this.dato);
			if (this.hijoIzquierdo != null)
			{
				this.hijoIzquierdo.postorden();
			}
			if (this.hijoDerecho != null)
			{
				this.hijoDerecho.postorden();
			}
		}

		public void recorridoPorNiveles()
		{
			Cola<ArbolBinario<T>> cola = new Cola<ArbolBinario<T>>();
			ArbolBinario<T> arbolTemp;
			cola.encolar(this);
			while (!cola.esVacia()) 
            {
				arbolTemp = cola.desencolar();
				Console.WriteLine(arbolTemp.getDatoRaiz());
				if (arbolTemp.getHijoIzquierdo() != null)
                {
					cola.encolar(arbolTemp.getHijoIzquierdo());
                }
				if (arbolTemp.getHijoDerecho() != null)
                {
					cola.encolar(getHijoDerecho());
                }
            }
		}

		public int contarHojas()
		{
			if (this.hijoIzquierdo != null && this.hijoDerecho != null)
            {
				return this.hijoIzquierdo.contarHojas() + this.hijoDerecho.contarHojas();
            }
			if (this.hijoIzquierdo != null && this.hijoDerecho == null)
            {
				return this.hijoIzquierdo.contarHojas();
            }
			if (this.hijoDerecho != null && this.hijoIzquierdo == null)
            {
				return this.hijoDerecho.contarHojas();
            }
			if (this.esHoja())
            {
				return 1;
            }
			return 0;
		}

		public void recorridoEntreNiveles(int n, int m)
		{
		}

	}
}
