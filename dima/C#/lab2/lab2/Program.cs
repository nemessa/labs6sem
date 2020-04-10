using System;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Collections.Generic;
using System.Xml;
using System.Xml.Serialization;

namespace lab2
{
    [Serializable]
    public partial class Graph {
        //kak zdelat Matrix-Lines -> Matrix-Line -> Weight?
        [XmlArray("Lines"), XmlArrayItem("Line")]
        public List< List<int> > matrix = new List< List<int> >();
        public Graph() : this(0) {}
        public Graph(int vertexAmount) {
            for(int i = 0; i < vertexAmount - 1; i++) {
                matrix.Add(new List<int>());
                for(int j = 0; j < vertexAmount - i - 1; j++) 
                    matrix[i].Add(0);
            }
        }

        private int[] NormalizedVertexes(int x, int y) => x > y ? new int[]{y, x} : new int[]{x, y};
        private int GetWeight(int[] vertexPair) => matrix[ vertexPair[0] ][ vertexPair[1] ];
        private void SetWeight(int[] vertexPair, int value) => matrix[ vertexPair[0] ][ vertexPair[1] ] = value;

        public int GetWeight(int x, int y) => GetWeight( NormalizedVertexes(x, y) );
        public void SetWeight(int x, int y, int value) => SetWeight(NormalizedVertexes(x,y), value);

        public void AddVertex() {
            matrix.Add(new List<int>());
            for(int i = 0; i < matrix.Count; i++)
                matrix[i].Add(0);
        }
    }

    public partial class Graph {
        public static void SerializeBinaryTo(Graph G, Stream st) => new BinaryFormatter().Serialize(st, G);
        public static Graph DeserializeFromBinary(Stream st) => (Graph) new BinaryFormatter().Deserialize(st);
        public static void SerializeXmlTo(Graph G, Stream st) => new XmlSerializer(typeof(Graph)).Serialize(st, G);
        public static Graph DeserializeFromXml(Stream st) => (Graph) new XmlSerializer(typeof(Graph)).Deserialize(st);
    }

    class Lab8 {
        public static void Main() {
            Graph G = new Graph(4);
            G.AddVertex();
            using (Stream st1 = new FileStream("somefile1.xml", FileMode.Open, FileAccess.Read) )
            using (Stream st2 = new FileStream("somefile2.xml", FileMode.Create) ) {
                Graph G1 = Graph.DeserializeFromXml(st1);
                Graph.SerializeXmlTo(G1, st2);
            }
        
            using(Stream st1 = new FileStream("somefile1.xml", FileMode.Open, FileAccess.Write) ) {
                Graph.SerializeXmlTo(G, st1);
            }
        }
    }
}