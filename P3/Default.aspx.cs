using System;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Web;
using System.Web.Security;
using System.Web.UI;
using System.Web.UI.HtmlControls;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Xml.Linq;

public partial class _Default : System.Web.UI.Page 
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        Class1 Obj = new Class1();

        int a = Convert.ToInt16(TextBox1.Text);

        int b = Convert.ToInt16(TextBox2.Text);

        Label1.Text = "Addition =>"+Obj.sum(a,b).ToString();


    }
    protected void Button2_Click(object sender, EventArgs e)
    {
        Class1 Obj = new Class1();

        int a = Convert.ToInt16(TextBox1.Text);

        int b = Convert.ToInt16(TextBox2.Text);

        Label1.Text = "Multiplicaton =>" + Obj.mul(a, b).ToString();
    }
}
