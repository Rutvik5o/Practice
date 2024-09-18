<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        Select product you want to purchase:</p>
    <p>
        <asp:CheckBoxList ID="CheckBoxList1" runat="server">
            <asp:ListItem>MotherBoard</asp:ListItem>
            <asp:ListItem>CPU</asp:ListItem>
            <asp:ListItem>SSD</asp:ListItem>
            <asp:ListItem>Graphic Card</asp:ListItem>
            <asp:ListItem>Pen Drive</asp:ListItem>
            <asp:ListItem>Spekaer</asp:ListItem>
        </asp:CheckBoxList>
    </p>
    <div>
    
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="Button" />
    <br />
    <br />
    <br />
    <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </form>
</body>
</html>
