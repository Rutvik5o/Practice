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
        if (Request.Cookies["multivalueCookies"] != null)
        {
            Label1.Text = "<b>Item No => " + Request.Cookies["multivalueCookies"]["Item no :"];

            Label2.Text = "<b> Item Name => " + Request.Cookies["multivalueCookies"]["Item Name :"];

            Label3.Text = "<b> Item Price => " + Request.Cookies["multivalueCookies"]["Item Price :"];

            Label4.Text = "<b> Item Qty => " + Request.Cookies["multivalueCookies"]["Item Qty :"];
        }
    }
}
