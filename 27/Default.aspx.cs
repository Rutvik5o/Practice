﻿using System;
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
        HttpCookie Obj = new HttpCookie("MyCookie");

        Obj.Values.Add("INo", TextBox1.Text);

        Obj.Values.Add("IName", TextBox2.Text);

        Obj.Values.Add("IQuantity", TextBox3.Text);

        Obj.Values.Add("IPrice", TextBox4.Text);

        Response.Cookies.Add(Obj);

        Response.Redirect("Default2.aspx");
    }
}