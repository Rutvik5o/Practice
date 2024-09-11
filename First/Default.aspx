<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        Select Product -&gt;
        <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="True" 
            DataSourceID="AccessDataSource1" DataTextField="ProductName" 
            DataValueField="ProductPrice">
        </asp:DropDownList>
        <asp:AccessDataSource ID="AccessDataSource1" runat="server" 
            DataFile="~/mainproduct.mdb" 
            SelectCommand="SELECT [ProductName], [ProductPrice] FROM [Table1]">
        </asp:AccessDataSource>
    </p>
    <p>
        Price -&gt;&nbsp;         <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </p>
    <p>
        &nbsp;</p>
    <p>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" 
            Text="Fetch Price" />
    </p>
    <p>
        &nbsp;</p>
    <p>
        Quantity -&gt;         <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
    </p>
    <p>
        Total Price :
        <asp:Label ID="Label2" runat="server" Text="Label"></asp:Label>
    </p>
    <p>
        &n&nbsp;</p>
    <p>
        <asp:Button ID="Button2" runat="server" onclick="Button2_Click" 
            Text="Calculate Price" />
    </p>
    <div>
    
    </div>
    </form>
</body>
</html>
