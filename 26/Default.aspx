<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    </div>
    <p>
        Select Image -&gt;&nbsp;
        <asp:FileUpload ID="FileUpload1" runat="server" />
    </p>
    <p>
        &nbsp;</p>
    <p>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="Upload" />
    </p>
    <p>
        &nbsp;</p>
    <p>
        &nbsp;</p>
    <p>
        <asp:DataList ID="DataList1" runat="server" RepeatColumns="5" 
            RepeatDirection="Horizontal">
            <ItemTemplate>
                <asp:Image ID="Image1" runat="server" Height="301px" 
                    ImageUrl='<%# Eval("Name","~/img/{0}") %>' Width="339px" />
            </ItemTemplate>
        </asp:DataList>
    </p>
    </form>
</body>
</html>
