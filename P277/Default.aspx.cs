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
        HttpCookie Cobj = new HttpCookie("multivalueCookies");

        Cobj.Values.Add("Item No :", TextBox1.Text);

        Cobj.Values.Add("Item Name :", TextBox2.Text);

        Cobj.Values.Add("Item Price :", TextBox3.Text);

        Cobj.Values.Add("Item Qty :", TextBox4.Text);

        Response.Cookies.Add(Cobj);

        Response.Redirect("Default2.aspx");





    }
}
