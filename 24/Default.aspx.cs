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
        int count = 1;

        if (Request.Cookies["MK"] != null)
        {
            count = Convert.ToInt16(Request.Cookies["MK"].Value);

            count++;
        }

        HttpCookie Obj = new HttpCookie("MK");

        Obj.Value = Convert.ToString(count);

        Response.Cookies.Add(Obj);

        Label1.Text = "You have visted total " + Convert.ToString(count) + " imes";

    
}
}
