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
        if (FileUpload1.HasFile)
        {
            if (FileUpload1.FileContent.Length < 1000000)
            {
                FileUpload1.SaveAs(Server.MapPath("~/imgs/" + FileUpload1.FileName));
            }
        }

    }

    protected void Page_PreRenderComplete(object sender, EventArgs e)
    {
        System.IO.DirectoryInfo Obj = new System.IO.DirectoryInfo(Server.MapPath("~/imgs"));

        DataList1.DataSource = Obj.GetFiles();

        DataList1.DataBind();
    }
}
