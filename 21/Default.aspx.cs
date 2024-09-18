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
        Label1.Text = DropDownList1.SelectedValue;
    }
    protected void Button2_Click(object sender, EventArgs e)
    {
     
        int tp;

        tp = Convert.ToInt32(Label1.Text) * Convert.ToInt32(TextBox1.Text);

        Label3.Text = Convert.ToString(tp);


    }
}
