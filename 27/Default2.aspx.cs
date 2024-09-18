using System;
using System.Collections;
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

public partial class Default2 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        if (Request.Cookies["MyCookie"] != null)
        {
            Label1.Text = "<b> Item No : <b>" + Request.Cookies["MyCookie"]["INo"];

            Label2.Text = "<b> Item Name : <b> " + Request.Cookies["MyCookie"]["IName"];

            Label3.Text = "<b> Item Quantity: <b> " + Request.Cookies["MyCookie"]["IQuantity"];

            Label4.Text = "<b> Item Price : <b> " + Request.Cookies["MyCookie"]["IPrice"];
        }
    }
}
